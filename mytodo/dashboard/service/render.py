from django.shortcuts import render
from django.http import HttpRequest


class RenderService:
    @staticmethod
    def render_name_display(request: HttpRequest):
        context: dict[str, str] = {"user": request.user}
        return render(request, "name_display.html", context)

    @staticmethod
    def render_phone_display(request: HttpRequest):
        context: dict[str, str] = {"user": request.user}
        return render(request, "phone_display.html", context)

    @staticmethod
    def render_bio_section(request: HttpRequest):
        context: dict[str, str] = {"user": request.user}
        return render(request, "bio_section.html", context)

    @staticmethod
    def render_dashboard_page(request: HttpRequest):
        return render(request, "dashboard.html")

    @staticmethod
    def render_edit_name_page(request: HttpRequest):
        context: dict[str, str] = {"user": request.user}
        return render(request, "edit_name.html", context)

    @staticmethod
    def render_edit_phone_page(request: HttpRequest):
        context: dict[str, str] = {"user": request.user}
        return render(request, "edit_phone.html", context)

    @staticmethod
    def render_edit_bio_page(request: HttpRequest):
        context: dict[str, str] = {"user": request.user}
        return render(request, "edit_bio.html", context)

    @staticmethod
    def edit_name(request: HttpRequest):
        user = request.user
        context: dict[str, str] = {"user": user}

        name = request.POST.get("name", "").strip()
        if name:
            user.username = name
            user.save()

        return render(request, "name_display.html", context)

    @staticmethod
    def edit_phone(request: HttpRequest):
        user = request.user

        phone_number: str = request.POST.get("phone_number", "").strip()
        user.phone_number = phone_number
        user.save()

        context: dict[str, str] = {"user": user}
        return render(request, "phone_display.html", context)

    @staticmethod
    def edit_bio(request: HttpRequest):
        user = request.user

        if request.method == "GET":
            context: dict[str, str] = {"user": user}
            return render(request, "edit_bio.html", context)

        if request.method == "POST":
            bio: str = request.POST.get("bio", "").strip()
            user.bio = bio
            user.save()

            context: dict[str, str] = {"user": user}
            return render(request, "bio_section.html", context)


render_service = RenderService()
