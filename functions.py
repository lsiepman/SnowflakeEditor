# Classes and functions

class Cards:
    """All functions connected to cards."""

    def __init__(self):
        self.cards = []

    def check_uploads(self):
        """Check if a document with was uploaded containing the cards."""
        pass

    def create_card(self):
        """Create a single card."""
        pass

    def fetch_card(self):
        """Fetch the data of a card."""
        pass

    def snowflake_card(self):
        """Use the snowflake method and replace one card with multiple others."""
        pass


class Characters:
    """All functions connected to characters."""

    def __init__(self):
        self.characters = {}
        self.template = {"Name": None, "Age": None, "Date of Birth": None, "Physical appearance": None, "Background": None,
                        "Relationships to others": None, "Story role": None, "Personal story arc (one sentence)": None,
                        "Character goal": None, "Character motivation": None, "Character conflict": None, "Lessons learned": None,
                        "Summary of story arc (paragraph)": None}

    def create_character(self):
        """Create a new character."""
        pass

    def edit_character(self):
        """Add new fields or edit existing fields."""
        pass

    def delete_character(self):
        """Remove a character."""
        pass

