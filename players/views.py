from django.shortcuts import render
from .models import Player
from .brawl import PlayerInfo

# Create your views here.
def all_players(request):
    if request.method == 'GET':
        player_tag = request.GET.get('playerTag', '')  # Get the playerTag from the submitted form

        if player_tag:
            try:
                # Initialize PlayerInfo class and fetch player information
                player_info_obj = PlayerInfo(player_tag)
                player_username = player_info_obj.username()
                player_trophies = player_info_obj.trophy_count()

                # Check if the player with the same username already exists in the database
                existing_player = Player.objects.filter(username=player_username).first()

                if not existing_player:
                    # If the player doesn't exist, create a new Player instance and save it
                    player_instance = Player(username=player_username, trophies=player_trophies)
                    player_instance.save()
                else:
                    # If the player already exists, update their trophies
                    existing_player.trophies = player_trophies
                    existing_player.save()
            except Exception as e:
                print(f"Error fetching or saving player data: {e}")
                render(request, 'all.html')
                
    players = Player.objects.all()
    return render(request, 'all.html', {'players': players})

def player_7eevvan(request):
    return render(request, '7eevan.html')