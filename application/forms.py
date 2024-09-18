from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'candidate', 
            'status', 
            'scores', 
            'cover_letter', 
            'interview_feedback', 
            'job'
        ]
        widgets = {
            'cover_letter': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'scores': forms.TextInput(attrs={'placeholder': 'Enter scores as JSON'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example of custom label or help text
        self.fields['cover_letter'].label = 'Cover Letter'
        self.fields['interview_feedback'].help_text = 'Provide any feedback received during the interview process.'

    def clean_scores(self):
        scores = self.cleaned_data.get('scores')
        # Example validation: Ensure 'scores' contains a specific key
        if 'total_score' not in scores:
            raise forms.ValidationError("Total score must be provided.")
        return scores
