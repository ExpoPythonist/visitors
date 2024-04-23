from secrets import choice
from django import forms
from visitors_app import models
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User


class SaveUser(UserCreationForm):
    username = forms.CharField(max_length=250, help_text="The Username field is required.")
    email = forms.EmailField(max_length=250, help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250, help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250, help_text="The Last Name field is required.")
    password1 = forms.CharField(max_length=250)
    password2 = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2',)


class UpdateProfile(UserChangeForm):
    username = forms.CharField(max_length=250, help_text="The Username field is required.")
    email = forms.EmailField(max_length=250, help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250, help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250, help_text="The Last Name field is required.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Password is Incorrect")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")


class UpdateUser(UserChangeForm):
    username = forms.CharField(max_length=250, help_text="The Username field is required.")
    email = forms.EmailField(max_length=250, help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250, help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250, help_text="The Last Name field is required.")

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")


class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}), label="Old Password")
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}), label="New Password")
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm rounded-0'}),
        label="Confirm New Password")

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class SaveDepartment(forms.ModelForm):
    name = forms.CharField(max_length=250)
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Departments
        fields = ('name', 'status',)

    def clean_name(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        name = self.cleaned_data['name']
        try:
            if id > 0:
                dept = models.Departments.objects.exclude(id=id).get(name=name, delete_flag=0)
            else:
                dept = models.Departments.objects.get(name=name, delete_flag=0)
        except:
            return name
        raise forms.ValidationError("Department Name already exists.")


class SaveVisitor(forms.ModelForm):
    department = forms.CharField(max_length=250)
    name = forms.CharField(max_length=250)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    contact = forms.CharField(max_length=250, required=False)
    email = forms.CharField(max_length=250, required=False)
    address = forms.Textarea()
    reason = forms.Textarea()

    class Meta:
        model = models.Visitors
        fields = ('name', 'department', 'gender', 'contact', 'email', 'address', 'reason',)

    def clean_department(self):
        did = self.cleaned_data['department'] if self.cleaned_data['department'].isnumeric() else 0
        try:
            if int(did) > 0:
                dept = models.Departments.objects.get(id=did)
                return dept
            else:
                raise forms.ValidationError("Selected Department is Invalid.")
        except:
            raise forms.ValidationError("Selected Department is Invalid.")
