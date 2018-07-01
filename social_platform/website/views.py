from django.shortcuts import get_object_or_404, render
from utilities.banksAPI.NBG import ibankDigitalPaymentsWallet



def index(request):
    """
    Η αρχική σελίδα.

    Εμφανίζει την αρχική σελίδα της πλατφόρμας.
    """

    # user = NBG("User2", 80)
    return render(request, 'website/index.html')