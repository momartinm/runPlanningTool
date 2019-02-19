(define (domain mine-vehicle)
 (:requirements :fluents :typing :durative-actions :duration-inequalities :adl :fluents)
 (:types vehicle location - object
           hideout - location)
 (:predicates
    (road ?l1 ?l2 - location)
    (free ?l  - location)
    (at ?x - vehicle ?y - location))

 (:functions (road-length ?l1 ?l2 - location))

 (:durative-action drive
    :parameters (?v - vehicle ?l1 ?l2 - location)
    :duration (= ?duration (road-length ?l1 ?l2))
    :condition (and 
                    (at start (free ?l2))
                    (at start (at ?v ?l1)))
    :effect (and
            (at start (not (at ?v ?l1)))
            (at end (at ?v ?l2))))

 )
