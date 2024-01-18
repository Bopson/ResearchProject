from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Player
from django.contrib.auth import authenticate, login, logout
from django import forms



    

class newForm(forms.Form):
        
        CHOICES = [
        ('goalKeeper', 'Goal Keeper'),
        ('defender', 'Defender'),
        ('midfielder', 'MidFielder'),
        ('forward', 'Forward'),
    ]



        first_name=forms.CharField(label="First_name", max_length=20)
        last_name=forms.CharField(label="Last_name", max_length=20)
        position = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        strength=forms.DecimalField(label="strength", min_value=0, max_value=10)
        speed=forms.DecimalField(label="speed", min_value=0, max_value=10)
        technique=forms.DecimalField(label="Technique", min_value=0, max_value=10)
        mindset=forms.DecimalField(label="Mindset", min_value=0, max_value=10)
        gameIntelligence=forms.DecimalField(label="Game Intelligence", min_value=0, max_value=10)
        teamPlayer=forms.DecimalField(label="Team Player", min_value=0, max_value=10)
        endurance=forms.DecimalField(label="Endurance", min_value=0, max_value=10)

class bestTeamF(forms.Form):
          goalKeeper=forms.IntegerField(label="GoalKeeper", min_value="0", max_value="1")
          defender = forms.IntegerField(label="Defender", min_value="0", max_value="5")
          miedFielder=forms.IntegerField(label="MidFielder", min_value="0", max_value="5")
          forward=forms.IntegerField(label="Forward", min_value="0", max_value="4")
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("manageplayersdata"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")
    

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message":"Logged Out."
    })
    
def manageplayersdata(request):
    return render(request, "users/manageplayers.html")

def createPlayer(request):

   

    if request.method=='POST':
        form = newForm(request.POST)
        if form.is_valid():
            first=form.cleaned_data['first_name']
            last=form.cleaned_data["last_name"]
            position =form.cleaned_data["position"]
            speed=form.cleaned_data["speed"]
            strength=form.cleaned_data["strength"]
            technique=form.cleaned_data["technique"]
            mindset=form.cleaned_data["mindset"]
            gameIntelligence=form.cleaned_data["gameIntelligence"]
            teamPlayer=form.cleaned_data["teamPlayer"]
            endurance=form.cleaned_data["endurance"]
            skill_level= (speed+strength+technique+mindset+gameIntelligence+teamPlayer+endurance)/7

        player = Player(first=first, last=last,position=position,strength=strength,speed=speed,technique=technique,mindset=mindset,gameIntelligence=gameIntelligence, teamPlayer=teamPlayer,endurance=endurance, skill_level=skill_level)
        player.save()
        return render(request, "users/createPlayer.html",{
            "form": newForm(),
            "message": "Player added successfully!"
            
        })

    return render(request, "users/createPlayer.html",{
        "form": newForm()
    })

def viewPlayers(request):
    players=Player.objects.all()
    return render(request, "users/viewPlayers.html",{
        "players":players
    })

def update_view(request, id):
    
        player = Player.objects.get(pk=id)
        form = newForm()
        return render(request, "users/update.html",{
            "form" : form
        })
    
   

def delete_view(request, id):
    Player.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse("viewPlayers"))

def bestTeamForm(request):
    
     return render(request, "users/bestTeamForm.html",{
          "form2": bestTeamF()
     })

def bestTeam(request):
 if request.method=="POST":
    form = bestTeamF(request.POST)
    
    
    def select_best_team(players, positions_needed):
        best_team = {}
        players.sort(key=lambda player: -player.skill_level)

        for player in players:
            position = player.position.lower()
            if position in positions_needed and positions_needed[position] > 0:
                best_team.setdefault(position, []).append(player)
                positions_needed[position] -= 1

        return best_team

    def print_best_team(best_team):
        for position, players in best_team.items():
            print(f"{position} (Count: {len(players)}):")
            for player in players:
                print(f"  {player.first} ({player.skill_level})")

# Create player objects
    players=[]
    for player in Player.objects.all():
        players.append(player)
    
# Define the number of players needed for each position
    positions_needed = {
    "goalkeeper": int(request.POST["goalKeeper"]),
    "defender": int(request.POST["defender"]),
    "midfielder": int(request.POST["miedFielder"]),
     "forward": int(request.POST["forward"]),
}

# Select the best team based on the number of players needed for each position
    best_team = select_best_team(players, positions_needed)

# Print the best team
    print_best_team(best_team)

 
    return render(request, "users/bestTeam.html",{
             "bestTeam":best_team
        })
 return render(request, "users/bestTeamForm.html")