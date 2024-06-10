class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {}
        self.history = []

    def update_preferences(self, key, value):
        self.preferences[key] = value

    def add_to_history(self, message):
        self.history.append(message)

    def get_profile(self):
        return {
            'user_id': self.user_id,
            'preferences': self.preferences,
            'history': self.history
        }

