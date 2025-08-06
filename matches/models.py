from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    crex_id = models.CharField(max_length=50, unique=True)
    team_a = models.ForeignKey(Team, related_name="team_a_matches", on_delete=models.CASCADE)
    team_b = models.ForeignKey(Team, related_name="team_b_matches", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    venue = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, default="upcoming")

    def __str__(self):
        return f"{self.team_a} vs {self.team_b} - {self.start_time}"

class Player(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LiveScore(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.FloatField(default=0.0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.match} - {self.runs}/{self.wickets} ({self.overs} overs)"
