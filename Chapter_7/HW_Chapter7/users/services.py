import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """ Создаем stripe продукт. """
    title_product = f"{instance.paid_course}" if instance.paid_course else instance.paid_lesson
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


def create_stripe_price(amount, stripe_product_id):
    """
   создает цену в страйп
    """
    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product_data={"name": "Payment"},
        # product=stripe_product_id,
    )


def create_stripe_session(price):
    """
    создает сессию на оплату в страйпе
    """
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
