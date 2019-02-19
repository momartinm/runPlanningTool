(define (problem mine-vehicle-1)
 (:domain mine-vehicle)
 (:objects
  loc1 - location
  loc2 - hideout
  truck1 - vehicle)
 (:init 
  (road loc1 loc2)
  (road loc2 loc1)
  (at truck1 loc1)
  (free loc2)
  (= (road-length loc1 loc2) 10)
  (= (road-length loc2 loc1) 10)
  )
 (:goal (and 
         (at truck1 loc2)))
 (:metric minimize (total-time)))
