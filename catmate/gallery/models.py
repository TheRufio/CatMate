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
    relation profile (user1<-profile->user2) #with achievements per day/season/game/ivent <3*
    # day/season/game/ivent/gallery/chat publication and so on.. think about it and carrency (for achievements)
    gallery (user1<-gallery->user2) optimization!!!!

    ~ Registration ~
        CustomUser:
            username
            firstname
            lastname
            age
            gender
        Profile:
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
    ~ Chat ~
        Chat:


    ~ Relation ~

    ~ Market ~


    # love and friend coin
    # recomendation system that mean:
    # Profile (user): interests like football, sport, programming...
    #
    # Applications: ~ registration  (username, password, email, gender, interests)
    #               ~ gallery       (photoes folder, special days...)
    #               + chat          (chats, speacial chat *with couple or friend after "CatLink"*)
    #               + relation      (friends, couple, achievements, love & friends coin)
    #               + market        (buy & sale: gifts, unique features... )
"""
