# models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)  # Ensure this is hashed in the form handling process
    github_url = models.URLField()

    def __str__(self):
        return self.username
def get_compatibility_score(self, other_profile):
        score = 0
        # Example logic: if both users have the same skills or GitHub repositories, increase score
        if self.skills == other_profile.skills:
            score += 50
        if self.github_url == other_profile.github_url:
            score += 30
        if self.experience_level == other_profile.experience_level:
            score += 20
        return score
class CodingDoubtSession(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Session for {self.user_profile.username}"        