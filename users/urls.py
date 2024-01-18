from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("login",views.login_view,name="login"),
    path("logout", views.logout_view, name="logout"),
    path("manageplayersdata", views.manageplayersdata,name="manageplayersdata"),
    path("manageplayersdata/bestTeamForm", views.bestTeamForm,name="bestTeamForm"),
    path("manageplayersdata/bestTeam", views.bestTeam,name="bestTeam"),
    path("manageplayersdata/createPlayer", views.createPlayer, name="createPlayer"),
    path("manageplayersdata/viewPlayers", views.viewPlayers, name="viewPlayers"),
    path("manageplayersdata/viewPlayers/<int:id>/update", views.update_view, name="update"),
    path("manageplayersdata/viewPlayers/<str:id>/delete", views.delete_view, name="delete")
]