from django import forms
class InsertDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product ID",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter Your Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter Your Product Class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    product_color = forms.CharField(
        label="Enter Your Product Color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_weight = forms.IntegerField(
        label="Enter Your Product Weight",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Weight'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Your Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )

class UpdatedataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product ID",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product ID'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Your Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )
class DeleteDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Your Product ID",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product ID'
            }
        )
    )
