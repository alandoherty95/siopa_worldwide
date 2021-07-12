from django.http import HttpResponse


class StripeWH_Handler:
    """Handles Stripe webhooks to notify
    application when an event happens"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic or unknown webhook events
        """
        return HttpResponse(
            content=f'Unhandled Stripe webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Stripe webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Stripe webhook received: {event["type"]}',
            status=200)
