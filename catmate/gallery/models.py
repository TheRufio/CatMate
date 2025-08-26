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

    # love and friend coin
    # recomendation system that mean:
    # Profile (user): interests like football, sport, programming...
    
"""
