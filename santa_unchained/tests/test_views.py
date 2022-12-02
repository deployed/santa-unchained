from django.urls import NoReverseMatch, resolve, reverse


class TestWishListSuccessView:
    def test_wishlist_success_url_exists(self):
        try:
            url = reverse("wishes:success", kwargs={"slug": "slug"})
        except NoReverseMatch:
            assert (
                False
            ), "Nie ma adresu URL o nazwie 'success' w aplikacji 'wishes' ('wishes:success'"
        assert url == "/wishes/success/slug/", "Adres URL 'success' nie jest poprawny"

        view = resolve(url)
        assert view.func.view_class.__name__ == "WishListSuccessView", "Widok ma złą nazwę"
        assert view.func.view_class.__module__ == "santa_unchained.wishes.views", "Widok znajduje się w złym plik"


class TestWishListFormView:

    def test_wishlist_form_url_exists(self):
        try:
            url = reverse("wishes:wishlist")
        except NoReverseMatch:
            assert (
                False
            ), "Nie ma adresu URL o nazwie 'wishlist' w aplikacji 'wishes' ('wishes:wishlist'"
        assert url == "/wishes/", "Adres URL 'wishlist' nie jest poprawny"

        view = resolve(url)
        assert view.func.view_class.__name__ == "WishListFormView", "Widok ma złą nazwę"
        assert view.func.view_class.__module__ == "santa_unchained.wishes.views", "Widok znajduje się w złym plik"


class TestWishListDetailView:

    def test_wishlist_detail_url_exists(self):
        try:
            url = reverse("wishes:wishlist-detail", kwargs={"slug": "slug"})
        except NoReverseMatch:
            assert (
                False
            ), "Nie ma adresu URL o nazwie 'wishlist-detail' w aplikacji 'wishes' ('wishes:wishlist-detail'"
        assert url == "/wishes/slug/", "Adres URL 'wishlist-detail' nie jest poprawny"

        view = resolve(url)
        assert view.func.view_class.__name__ == "WishListDetailView", "Widok ma złą nazwę"
        assert view.func.view_class.__module__ == "santa_unchained.wishes.views", "Widok znajduje się w złym pliku"
