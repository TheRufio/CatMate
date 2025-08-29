from django.db import models

"""
    ~ Profile ~
    profile (user)

    ~ Home ~
    chats (chat1, chat2...)
 -->chat (user1->group<-user2) #OneToOne
 |   
 |  ~ Relations ~
 -->chat (user1->group<-user2) #special <3*
    relation (user1->group<-user2)
    relation profile (user1<-profile->user2) #with achievements per day/season/game/event <3*
    # day/season/game/ivent/gallery/chat publication and so on.. think about it and carrency (for achievements)
    gallery (user1<-gallery->user2) optimization!!!!

    ~ Registration ~
        CustomUser:
            *username
            *firstname
            *lastname


        UserProfile:
            age
            gender
            chats
            special chats
            galleries
            interests

            
    ~ Gallery ~
        Gallery:
            image
            description
            relation
            date
            is_special_day   
    ~ Main ~
        


    ~ Relation ~

    ~ Market ~


    # love and friend coin
    # recomendation system that mean:
    # Profile (user): interests like football, sport, programming...
    #
    # Applications: ~ registration  (username, password, email, gender, interests)
    #               + main          (chats, speacial chat *with love or friend after "CatLink"*)
    #               ~ gallery       (photoes folder, special days...)
    #               + relation      (friends, love, achievements, love & friends coin)
    #               + marketplace   (buy & sale: gifts, unique features... )
    #               + event         (daily/monthly/yers/season events and mini games)
"""
