"""
Forms for user registration, authentication, profile updates, and password changes.
"""

import re
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from apps.accounts.models import User, UserProfile


class UserRegistrationForm(forms.ModelForm):
    """
    User registration form with strict local validation, password confirmation,
    and phone number formatting.
    """
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter strong password'}),
        help_text="At least 8 characters with letters, numbers, and symbols."
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter password'})
    )
    terms_accepted = forms.BooleanField(
        required=True,
        label="I agree to the local health privacy terms and conditions.",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. john_doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. john@example.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. +1 555-0199'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email address already exists.")
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number', '').strip()
        if phone:
            # Allow digits, spaces, plus, hyphens, parentheses
            if not re.match(r'^[+]?[\d\s\-()]{7,20}$', phone):
                raise ValidationError("Please enter a valid phone number (7 to 20 digits).")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        confirm_pwd = cleaned_data.get('confirm_password')

        if pwd and confirm_pwd:
            if pwd != confirm_pwd:
                self.add_error('confirm_password', "Passwords do not match.")
            else:
                validate_password(pwd)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """
    Login form accepting either username or email address, with remember-me capability.
    """
    username_or_email = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email',
            'autofocus': 'autofocus'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Remember this device"
    )

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get('username_or_email', '').strip()
        password = cleaned_data.get('password', '')

        if identifier and password:
            # Check if identifier is email
            username = identifier
            if '@' in identifier:
                try:
                    user_obj = User.objects.get(email__iexact=identifier)
                    username = user_obj.username
                except User.DoesNotExist:
                    pass

            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError("Invalid credentials. Please verify your username/email and password.")
            if not user.is_active:
                raise ValidationError("This account is currently deactivated. Please contact an administrator.")
            if user.is_locked():
                raise ValidationError("Account is temporarily locked due to multiple failed login attempts.")
            cleaned_data['user'] = user

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    """
    Form for updating personal medical demographics, contact details, and emergency info.
    """
    first_name = forms.CharField(
        max_length=150, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=150, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=25, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserProfile
        fields = [
            'date_of_birth', 'gender', 'blood_group', 'avatar',
            'address', 'city', 'state', 'postal_code', 'country',
            'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relation',
            'session_timeout_minutes', 'preferred_theme', 'time_format', 'date_format',
            'enable_sound_notifications'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_relation': forms.TextInput(attrs={'class': 'form-control'}),
            'session_timeout_minutes': forms.NumberInput(attrs={'class': 'form-control', 'min': 5, 'max': 480}),
            'preferred_theme': forms.Select(attrs={'class': 'form-select'}),
            'time_format': forms.Select(attrs={'class': 'form-select'}),
            'date_format': forms.Select(attrs={'class': 'form-select'}),
            'enable_sound_notifications': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['phone_number'].initial = self.instance.user.phone_number

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.phone_number = self.cleaned_data.get('phone_number', '')
        if commit:
            user.save()
            profile.save()
        return profile


class UserPasswordChangeForm(forms.Form):
    """
    Allows authenticated users to securely update their password.
    """
    current_password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter current password'})
    )
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'})
    )
    confirm_new_password = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_current_password(self):
        current_pwd = self.cleaned_data.get('current_password')
        if not self.user.check_password(current_pwd):
            raise ValidationError("Current password does not match.")
        return current_pwd

    def clean(self):
        cleaned_data = super().clean()
        new_pwd = cleaned_data.get('new_password')
        confirm_pwd = cleaned_data.get('confirm_new_password')

        if new_pwd and confirm_pwd:
            if new_pwd != confirm_pwd:
                self.add_error('confirm_new_password', "New passwords do not match.")
            else:
                validate_password(new_pwd, user=self.user)
        return cleaned_data

    def save(self):
        new_password = self.cleaned_data['new_password']
        self.user.set_password(new_password)
        self.user.save()
        return self.user
