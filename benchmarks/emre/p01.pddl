(define (problem mine-vehicle-big)
(:domain mine-vehicle)
  (:objects
    loc0 - location
    loc1 - location
    loc2 - location
    loc3 - location
    loc4 - location
    loc5 - location
    loc6 - location
    loc7 - location
    loc8 - location
    loc9 - location
    truck0 - vehicle
    truck3 - vehicle
    truck1 - vehicle
    truck2 - vehicle
  )
  (:init
    (road loc0 loc1)
    (road loc1 loc0)
    (= (road-length loc0 loc1) 22)
    (= (road-length loc1 loc0) 12)
    (is-hideout loc1)
    (available loc1)
    (road loc1 loc2)
    (road loc2 loc1)
    (= (road-length loc1 loc2) 25)
    (= (road-length loc2 loc1) 26)
    (is-hideout loc2)
    (available loc2)
    (road loc2 loc3)
    (road loc3 loc2)
    (= (road-length loc2 loc3) 7)
    (= (road-length loc3 loc2) 27)
    (is-hideout loc3)
    (available loc3)
    (road loc3 loc4)
    (road loc4 loc3)
    (= (road-length loc3 loc4) 29)
    (= (road-length loc4 loc3) 14)
    (is-hideout loc4)
    (available loc4)
    (road loc4 loc5)
    (road loc5 loc4)
    (= (road-length loc4 loc5) 12)
    (= (road-length loc5 loc4) 27)
    (is-hideout loc5)
    (available loc5)
    (road loc5 loc6)
    (road loc6 loc5)
    (= (road-length loc5 loc6) 5)
    (= (road-length loc6 loc5) 24)
    (road loc6 loc7)
    (road loc7 loc6)
    (= (road-length loc6 loc7) 21)
    (= (road-length loc7 loc6) 23)
    (road loc7 loc8)
    (road loc8 loc7)
    (= (road-length loc7 loc8) 29)
    (= (road-length loc8 loc7) 11)
    (road loc8 loc9)
    (road loc9 loc8)
    (= (road-length loc8 loc9) 16)
    (= (road-length loc9 loc8) 5)
    (on-road truck0)
    (on-road truck3)
    (= (vehicle-speed truck0) 3)
    (= (hide-duration truck0) 10)
    (= (vehicle-speed truck3) 3)
    (= (hide-duration truck3) 5)
    (at truck0 loc0)
    (at truck3 loc9)
    (on-road truck1)
    (= (vehicle-speed truck1) 2)
    (= (hide-duration truck1) 5)
    (at truck1 loc8)
    (on-road truck2)
    (= (vehicle-speed truck2) 2)
    (= (hide-duration truck2) 6)
    (at truck2 loc1)
    (busy loc0)
    (busy loc1)
    (free loc2)
    (free loc3)
    (free loc4)
    (free loc5)
    (free loc6)
    (free loc7)
    (busy loc8)
    (busy loc9)
  )
(:goal (and (at truck0 loc9)(at truck3 loc0)))
  (:metric minimize (total-time)))