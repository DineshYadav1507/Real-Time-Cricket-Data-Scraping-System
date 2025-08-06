from django.shortcuts import render, get_object_or_404
from .models import Match, LiveScore
from .scraping import fetch_upcoming_matches

def match_list(request):
    matches = Match.objects.all().order_by("start_time")
    return render(request, "match_list.html", {"matches": matches})

def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    live_score = LiveScore.objects.filter(match=match).first()
    return render(request, "match_detail.html", {"match": match, "live_score": live_score})

def scrape_and_update(request):
    matches = fetch_upcoming_matches()
    return render(request, "scraped_data.html", {"matches": matches})
