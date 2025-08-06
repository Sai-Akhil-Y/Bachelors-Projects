#lang racket

;Defining 2 lists for numbers and symbols of a deck
(define numbers '(2 3 4 5 6 7 8 9 10 J Q K A))
(define symbols '(spade club heart diamond))

;Procedure to get all the different cards
(define (create-deck nums symbs)
  (define (outer-loop nums symbs)
    (cond
      ((null? nums)
       '())
      (else
       (append (inner-loop (car nums) symbs)
               (outer-loop (cdr nums) symbs)))))

  (define (inner-loop x symbs)
    (cond
      ((null? symbs)
       '())
      (else
       (cons (cons x (car symbs)) 
             (inner-loop x (cdr symbs))))))

  (outer-loop nums symbs))
;Storing all 52 cards in a variablesn
(define full-deck (create-deck numbers symbols))

;Alternative version to get 52 cards using inbuilt functions
(define full-deck-2 (cartesian-product numbers symbols))

;To get length of list
(define (list-length list)
  (define (iter list len)
    (if (null? list) len
        (iter (cdr list) (add1 len))))
  (iter list 0))

;To create a shuffled deck using basic loop
(define (shuffle-deck deck)
  (define (loop list-1 list-2 n)
    (if (= n 0) (cons (car list-1) (shuffle-deck (append (cdr list-1) list-2)))
                (loop (cdr list-1) (cons (car list-1) list-2) (sub1 n))))
  (if (null? deck)
      '()
      (loop deck '() (random (list-length deck)))))
(define shuffled-deck (shuffle-deck full-deck))


;To create a shuffled deck using inbuilt function
(define shuffled-deck-2 (shuffle full-deck))

;To count number of aces in a deck
(define (ace-count deck)
    (define (iter list result)
      (cond ((null? list) result)
            ((equal? (caar list) 'A) (iter (cdr list) (add1 result)))
            (else (iter (cdr list) result))))
    (iter deck 0))

;To count the card total based on 21 to win
(define (count-total-21 list)
  (let ((track-aces (ace-count list))
        (count 0) 
        (alt-count 0))
    (define (adjust-counts-for-aces)
      (if (>= track-aces 1)
          (cond ((= track-aces 1) (begin (set! count (+ 11 count));Ace can be 11 or 1 so we maintain 2 counts to see which is suitable for players cards
                                         (set! alt-count (add1 alt-count))
                                         (tally)))
                ((= track-aces 2) (begin (set! count (+ 12 count))
                                         (set! alt-count (+ 2 alt-count))
                                         (tally)))
                ((= track-aces 3) (begin (set! count (+ 13 count))
                                         (set! alt-count (+ 3 alt-count))
                                         (tally)))
                ((= track-aces 4) (begin (set! count (+ 14 count))
                                         (set! alt-count (+ 4 alt-count))
                                         (tally)))
                (else "this case will never come"))
          count))
    (define (tally)
      (if (>= 21 count) count
           alt-count))
    (define (iter list-1)
      (cond ((null? list-1) (adjust-counts-for-aces))
            ((eq? (caar list-1) 'A) (iter (cdr list-1)))   
            ((or (eq? (caar list-1) 'K)
                 (eq? (caar list-1) 'Q)
                 (eq? (caar list-1) 'J)) (begin (set! count (+ count 10));for K Q J we are adding 10 to score as the value of those cards is 10
                                                (set! alt-count (+ alt-count 10))
                                                (iter (cdr list-1))))
            (else (begin (set! count (+ (caar list-1) count))
                         (set! alt-count (+ (caar list-1) alt-count))
                         (iter (cdr list-1))))))
    (iter list)))

;To count the card total based on 17 to win
(define (count-total-17 list)
  (let ((track-aces (ace-count list))
        (count 0) 
        (alt-count 0))
    (define (adjust-counts-for-aces)
      (if (>= track-aces 1)
          (cond ((= track-aces 1) (begin (set! count (+ 11 count));Ace can be 11 or 1 so we maintain 2 counts to see which is suitable for dealers cards
                                         (set! alt-count (+ 1 alt-count))
                                         (tally)))
                ((= track-aces 2) (begin (set! count (+ 12 count))
                                         (set! alt-count (+ 2 alt-count))
                                         (tally)))
                ((= track-aces 3) (begin (set! count (+ 13 count))
                                         (set! alt-count (+ 3 alt-count))
                                         (tally)))
                ((= track-aces 4) (begin (set! count (+ 14 count))
                                         (set! alt-count (+ 4 alt-count))
                                         (tally)))
                (else "redundant condition code wont reach to this"))
          count))
    (define (tally)
      (if (>= 17 count) count
           alt-count))
    (define (iter list-1)
      (cond ((null? list-1) (adjust-counts-for-aces))
            ((eq? (caar list-1) 'A) (iter (cdr list-1)));we are ignoring the ace count for now   
            ((or (eq? (caar list-1) 'K)
                 (eq? (caar list-1) 'Q)
                 (eq? (caar list-1) 'J)) (begin (set! count (+ count 10));for K Q J we are adding 10 to score as the value of those cards is 10
                                                (set! alt-count (+ alt-count 10))
                                                (iter (cdr list-1))))
            (else (begin (set! count (+ (caar list-1) count))
                         (set! alt-count (+ (caar list-1) alt-count))
                         (iter (cdr list-1))))))
    (iter list)))

;Main game flow
(define (start-game)
  (let ((deck (shuffle full-deck)))
    (let ((player (cons (car deck) (cons (caddr deck) '())))
          (dealer (cons (cadr deck) (cons (cadddr deck) '()))))
      (display "Dealer shows one of his card")
      (newline)
      (display (car dealer));only 1 card of dealer is shown
      (newline)
      (display "You have")
      (newline)
      (display player);all cards of player are shown
      (newline)
      (set! deck (cddddr deck));setting the deck pointing to 5th card
      (define (iter)
        (newline)
        (display "Do you want to hit?(yes / no)");asking the player whether he wants to take new card or not
        (newline)
        (let ((answer (read)))
          (cond ((eq? answer 'yes) 
                 (begin (set! player (cons (car deck) player));new card added to player cards
                                     (display player)
                                     (cond ((and (> (count-total-21 player) 21) (newline) "You Lose! (your cards count crossed 21)"));when player crosses 21
                                           ((< (count-total-21 player) 21) (begin (newline)
                                                                                  (set! deck (cdr deck));when the score  is still <21 player is asked again
                                                                                  (iter)))
                                           (else (iter)))))
                ((eq? answer 'no)
                 (cond ((and (equal? (count-total-21 player) 21) (= 2 (list-length player)));when you get ans A card and a 10 value card then its blackjack
                             "BLACKJACK!!! (you got score 21 in 2 cards)")
                       ((= (count-total-21 player) 21) (dealer-finishes-game));when you get 21 by more than 2 cards dealer count is checked
                       (else (dealer-finishes-game))))
                (else "fail- you have not typed yes / no"))))
      (define (dealer-finishes-game);this part does the finish side of dealer
        (newline)
        (display "Dealer shows his cards")
        (newline)
        (display dealer)
        (newline)
        (cond ((> (count-total-17 dealer) 17) "YOU WON!! (dealer score crossed 17)"); if dealer crosses 17 he loses
              ((and (= 17 (count-total-17 dealer)) (= 21 (count-total-21 player))) "Draw!");if both reach their equivalent high scores then its a draw
              ((and (equal? (count-total-17 dealer) 17) (= 2 (list-length dealer))) "Dealer Blackjack!!");if dealer score alone reaches 17 then its dealer blackjack
              ((and (> (count-total-17 dealer) (count-total-21 player)) "DEALER WINS!!! "));if dealer reaches 17 or if dealer's score is greater than player's then dealer wins
              (else (< (count-total-17 dealer) 17) (begin (set! dealer (cons (car deck) dealer))
                                                             (set! deck (cdr deck))
                                                             (newline)
                                                             (display "Dealer is Hitting");if dealers count is < 17 then he hits
                                                             (dealer-finishes-game)))))                                                                                       
      (iter))))