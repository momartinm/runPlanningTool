(define (domain mine-vehicle)
 (:requirements :typing :durative-actions :numeric-fluents)
 (:types vehicle location hideout - object)
 (:predicates
    (free ?l - location)
    (busy ?l - location)
    (road ?l1 ?l2 - location)
    (available ?l - location)
    (occupied ?l - location)
    (hidden ?v - vehicle)
    (is-hideout ?l - location)
    (on-road ?v - vehicle)
    (at ?x - vehicle ?y - location))
 
 (:functions 
    (road-length ?l1 ?l2 - location)
    (vehicle-speed ?v - vehicle)
    (hide-duration ?v - vehicle))

 (:durative-action drive
    :parameters (?v - vehicle ?l1 ?l2 - location)
    :duration (= ?duration (road-length ?l1 ?l2))
    :condition (and
            (at start (free ?l2))
            (at start (busy ?l1))
            (at start (at ?v ?l1))
            (at start (on-road ?v))
            (at start (road ?l1 ?l2)))
    :effect (and
            (at start (not (free ?l2)))
            (at start (not (busy ?l1)))
            (at start (not (at ?v ?l1)))
            (at start (free ?l1))
            (at start (busy ?l2))
            (at end (at ?v ?l2))))

  (:durative-action hide
    :parameters (?v - vehicle ?l - location)
    :duration (= ?duration (hide-duration ?v))
    :condition (and
            (at start (is-hideout ?l))
            (at start (at ?v ?l))
            (at start (on-road ?v))
            (at start (busy ?l))
            (at start (available ?l)))
    :effect (and
            (at start (not (busy ?l)))
            (at start (not (on-road ?v)))
            (at start (not (available ?l)))
            (at start (free ?l))
            (at end (occupied ?l))
            (at end (hidden ?v))))

  (:durative-action unhide
    :parameters (?v - vehicle ?l - location)
    :duration (= ?duration (hide-duration ?v))
    :condition (and 
            (at start (is-hideout ?l))
            (at start (at ?v ?l))
            (at start (occupied ?l))
            (at start (hidden ?v))
            (at start (free ?l)))
    :effect (and 
            (at start (not (hidden ?v)))
            (at start (not (free ?l)))
            (at start (not (occupied ?l)))
            (at start (busy ?l))
            (at end (available ?l))
            (at end (on-road ?v))))
 )
