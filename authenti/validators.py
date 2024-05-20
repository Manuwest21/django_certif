from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit être original au possible, nous accepterons rien en dehors des mots de passe originaux, compris?'