

(define (problem BW-rand-23)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 )
(:init
(on-table b1)
(on-table b2)
(on b3 b9)
(on b4 b15)
(on b5 b18)
(on b6 b4)
(on b7 b14)
(on-table b8)
(on b9 b21)
(on b10 b2)
(on b11 b17)
(on-table b12)
(on b13 b10)
(on b14 b11)
(on b15 b8)
(on b16 b12)
(on b17 b13)
(on b18 b23)
(on-table b19)
(on b20 b6)
(on b21 b20)
(on-table b22)
(on b23 b16)
(clear b1)
(clear b3)
(clear b5)
(clear b7)
(clear b19)
(clear b22)
)
(:goal
(and
(on b1 b2)
(on b2 b4)
(on b3 b17)
(on b4 b23)
(on b7 b19)
(on b8 b13)
(on b9 b3)
(on b10 b12)
(on b12 b9)
(on b13 b5)
(on b14 b21)
(on b15 b6)
(on b16 b1)
(on b17 b18)
(on b19 b8)
(on b20 b14)
(on b21 b11)
(on b22 b16)
(on b23 b7))
)
)

