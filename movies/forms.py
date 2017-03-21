from django import forms


class searchForm(forms.Form):
    title = forms.CharField(max_length=50, label='Title')


class addForm(forms.Form):
    titles = forms.CharField(max_length=50, label='Title')


class searchWatchlistForm(forms.Form):
    genre = forms.CharField(required=False, max_length=50, label='Genre')
    actors = forms.CharField(required=False, max_length=500, label='Actors')
    is_watched = forms.BooleanField(required=False, label='Is watched')


class isWatchedForm(forms.Form):
    is_watched = forms.BooleanField(required=False, label='Is watched')
