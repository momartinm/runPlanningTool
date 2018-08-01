(define (problem p5)
 (:domain floor-tile)
 (:objects tile_0-1 tile_0-2 tile_0-3 tile_0-4 tile_0-5 
           tile_1-1 tile_1-2 tile_1-3 tile_1-4 tile_1-5 
           tile_2-1 tile_2-2 tile_2-3 tile_2-4 tile_2-5 
           tile_3-1 tile_3-2 tile_3-3 tile_3-4 tile_3-5 
           tile_4-1 tile_4-2 tile_4-3 tile_4-4 tile_4-5 
           tile_5-1 tile_5-2 tile_5-3 tile_5-4 tile_5-5 - tile
           robot1 robot2 robot3 - robot
           white black - color
)
 (:init 
   (robot-at robot1 tile_2-3)
   (robot-has robot1 white)
   (robot-at robot2 tile_5-1)
   (robot-has robot2 black)
   (robot-at robot3 tile_1-2)
   (robot-has robot3 white)
   (available-color white)
   (available-color black)
   (clear tile_0-1)
   (clear tile_0-2)
   (clear tile_0-3)
   (clear tile_0-4)
   (clear tile_0-5)
   (clear tile_1-1)
   (clear tile_1-3)
   (clear tile_1-4)
   (clear tile_1-5)
   (clear tile_2-1)
   (clear tile_2-2)
   (clear tile_2-4)
   (clear tile_2-5)
   (clear tile_3-1)
   (clear tile_3-2)
   (clear tile_3-3)
   (clear tile_3-4)
   (clear tile_3-5)
   (clear tile_4-1)
   (clear tile_4-2)
   (clear tile_4-3)
   (clear tile_4-4)
   (clear tile_4-5)
   (clear tile_5-2)
   (clear tile_5-3)
   (clear tile_5-4)
   (clear tile_5-5)
   (tile-up tile_1-1 tile_0-1)
   (tile-up tile_1-2 tile_0-2)
   (tile-up tile_1-3 tile_0-3)
   (tile-up tile_1-4 tile_0-4)
   (tile-up tile_1-5 tile_0-5)
   (tile-up tile_2-1 tile_1-1)
   (tile-up tile_2-2 tile_1-2)
   (tile-up tile_2-3 tile_1-3)
   (tile-up tile_2-4 tile_1-4)
   (tile-up tile_2-5 tile_1-5)
   (tile-up tile_3-1 tile_2-1)
   (tile-up tile_3-2 tile_2-2)
   (tile-up tile_3-3 tile_2-3)
   (tile-up tile_3-4 tile_2-4)
   (tile-up tile_3-5 tile_2-5)
   (tile-up tile_4-1 tile_3-1)
   (tile-up tile_4-2 tile_3-2)
   (tile-up tile_4-3 tile_3-3)
   (tile-up tile_4-4 tile_3-4)
   (tile-up tile_4-5 tile_3-5)
   (tile-up tile_5-1 tile_4-1)
   (tile-up tile_5-2 tile_4-2)
   (tile-up tile_5-3 tile_4-3)
   (tile-up tile_5-4 tile_4-4)
   (tile-up tile_5-5 tile_4-5)
   (tile-down tile_0-1 tile_1-1)
   (tile-down tile_0-2 tile_1-2)
   (tile-down tile_0-3 tile_1-3)
   (tile-down tile_0-4 tile_1-4)
   (tile-down tile_0-5 tile_1-5)
   (tile-down tile_1-1 tile_2-1)
   (tile-down tile_1-2 tile_2-2)
   (tile-down tile_1-3 tile_2-3)
   (tile-down tile_1-4 tile_2-4)
   (tile-down tile_1-5 tile_2-5)
   (tile-down tile_2-1 tile_3-1)
   (tile-down tile_2-2 tile_3-2)
   (tile-down tile_2-3 tile_3-3)
   (tile-down tile_2-4 tile_3-4)
   (tile-down tile_2-5 tile_3-5)
   (tile-down tile_3-1 tile_4-1)
   (tile-down tile_3-2 tile_4-2)
   (tile-down tile_3-3 tile_4-3)
   (tile-down tile_3-4 tile_4-4)
   (tile-down tile_3-5 tile_4-5)
   (tile-down tile_4-1 tile_5-1)
   (tile-down tile_4-2 tile_5-2)
   (tile-down tile_4-3 tile_5-3)
   (tile-down tile_4-4 tile_5-4)
   (tile-down tile_4-5 tile_5-5)
   (tile-right tile_0-2 tile_0-1)
   (tile-right tile_0-3 tile_0-2)
   (tile-right tile_0-4 tile_0-3)
   (tile-right tile_0-5 tile_0-4)
   (tile-right tile_1-2 tile_1-1)
   (tile-right tile_1-3 tile_1-2)
   (tile-right tile_1-4 tile_1-3)
   (tile-right tile_1-5 tile_1-4)
   (tile-right tile_2-2 tile_2-1)
   (tile-right tile_2-3 tile_2-2)
   (tile-right tile_2-4 tile_2-3)
   (tile-right tile_2-5 tile_2-4)
   (tile-right tile_3-2 tile_3-1)
   (tile-right tile_3-3 tile_3-2)
   (tile-right tile_3-4 tile_3-3)
   (tile-right tile_3-5 tile_3-4)
   (tile-right tile_4-2 tile_4-1)
   (tile-right tile_4-3 tile_4-2)
   (tile-right tile_4-4 tile_4-3)
   (tile-right tile_4-5 tile_4-4)
   (tile-right tile_5-2 tile_5-1)
   (tile-right tile_5-3 tile_5-2)
   (tile-right tile_5-4 tile_5-3)
   (tile-right tile_5-5 tile_5-4)
   (tile-left tile_0-1 tile_0-2)
   (tile-left tile_0-2 tile_0-3)
   (tile-left tile_0-3 tile_0-4)
   (tile-left tile_0-4 tile_0-5)
   (tile-left tile_1-1 tile_1-2)
   (tile-left tile_1-2 tile_1-3)
   (tile-left tile_1-3 tile_1-4)
   (tile-left tile_1-4 tile_1-5)
   (tile-left tile_2-1 tile_2-2)
   (tile-left tile_2-2 tile_2-3)
   (tile-left tile_2-3 tile_2-4)
   (tile-left tile_2-4 tile_2-5)
   (tile-left tile_3-1 tile_3-2)
   (tile-left tile_3-2 tile_3-3)
   (tile-left tile_3-3 tile_3-4)
   (tile-left tile_3-4 tile_3-5)
   (tile-left tile_4-1 tile_4-2)
   (tile-left tile_4-2 tile_4-3)
   (tile-left tile_4-3 tile_4-4)
   (tile-left tile_4-4 tile_4-5)
   (tile-left tile_5-1 tile_5-2)
   (tile-left tile_5-2 tile_5-3)
   (tile-left tile_5-3 tile_5-4)
   (tile-left tile_5-4 tile_5-5)
)
 (:goal (and
    (painted tile_1-1 white)
    (painted tile_1-2 black)
    (painted tile_1-3 white)
    (painted tile_1-4 black)
    (painted tile_1-5 white)
    (painted tile_2-1 black)
    (painted tile_2-2 white)
    (painted tile_2-3 black)
    (painted tile_2-4 white)
    (painted tile_2-5 black)
    (painted tile_3-1 white)
    (painted tile_3-2 black)
    (painted tile_3-3 white)
    (painted tile_3-4 black)
    (painted tile_3-5 white)
    (painted tile_4-1 black)
    (painted tile_4-2 white)
    (painted tile_4-3 black)
    (painted tile_4-4 white)
    (painted tile_4-5 black)
    (painted tile_5-1 white)
    (painted tile_5-2 black)
    (painted tile_5-3 white)
    (painted tile_5-4 black)
    (painted tile_5-5 white)
))
 (:metric minimize (total-time))
)
