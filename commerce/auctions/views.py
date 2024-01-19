from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Item


@login_required
def index(request):
    items = Item.objects.all()
    return render(
        request,
        "auctions/index.html",
        {
            "items": items,
        },
    )


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new_listing(request):
    return render(request, "auctions/new_listing.html")


def save_listing(request):
    if request.method == "POST":
        item_name = request.POST["item_name"]
        item_price = request.POST["item_price"]
        item_description = request.POST["item_description"]
        item_image = request.POST["item_image"]
        item_category = request.POST["item_category"]

        item = Item(
            name=item_name,
            price=item_price,
            description=item_description,
            image=item_image,
            category=item_category,
        )
        item.save()
        items = Item.objects.all()
        return HttpResponseRedirect(reverse("index"))


# listing page
# need model with
# product, date created, number of people
# would need a form that will post category, image, description, and price also title and time and date created
# Every user should see this and be able to make a bid on the item
# bid
# show number of people that have bid on it
# show if youre winning the bid
# show the owner of the item
# watchlist page
# shows items you have put a bid on
# create listings
# you should be able to add items
