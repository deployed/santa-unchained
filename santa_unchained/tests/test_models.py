import pytest
from django.db.models import (
    BigAutoField,
    BooleanField,
    CharField,
    DecimalField,
    EmailField,
    ForeignKey,
    TextField,
)
from django_extensions.db.fields import AutoSlugField

from santa_unchained.wishes import models

Address = getattr(models, "Address", None)
assert Address is not None, "Model Address jest niezdefiniowany"

WishList = getattr(models, "WishList", None)
assert WishList is not None, "Model WishList jest niezdefiniowany"

WishListItem = getattr(models, "WishListItem", None)
assert WishListItem is not None, "Model WishListItem jest niezdefiniowany"


@pytest.mark.django_db()
class TestAddressModel:
    def test_address_has_all_neccessary_fields(self):
        assert {field.name for field in Address._meta.fields} == {
            "id",
            "street",
            "post_code",
            "city",
            "country",
            "lng",
            "lat",
        }, "Model Address nie ma wszystkich wymaganych pól"

    def test_field_types(self):
        types_map = {
            "id": BigAutoField,
            "street": CharField,
            "post_code": CharField,
            "city": CharField,
            "country": CharField,
            "lng": DecimalField,
            "lat": DecimalField,
        }
        for field in Address._meta.fields:
            assert isinstance(
                field, types_map[field.name]
            ), f"Pole '{field.name}' nie jest typu {types_map[field.name]}"


class TestWishListModel:
    def test_wishlist_has_all_neccessary_fields(self):
        assert {field.name for field in WishList._meta.fields} == {
            "id",
            "name",
            "email",
            "content",
            "status",
            "slug",
            "address",
        }, "Model WishList nie ma wszystkich wymaganych pól"

    def test_field_types(self):
        types_map = {
            "id": BigAutoField,
            "name": CharField,
            "email": EmailField,
            "content": TextField,
            "status": CharField,
            "slug": AutoSlugField,
            "address": ForeignKey,
        }
        for field in WishList._meta.fields:
            assert isinstance(
                field, types_map[field.name]
            ), f"Pole '{field.name}' nie jest typu {types_map[field.name]}"


class TestWishListItemModel:
    def test_wishlistitem_has_all_neccessary_fields(self):
        assert {field.name for field in WishListItem._meta.fields} == {
            "id",
            "wish_list",
            "name",
            "approved",
        }, "Model WishListItem nie ma wszystkich wymaganych pól"

    def test_field_types(self):
        types_map = {
            "id": BigAutoField,
            "wish_list": ForeignKey,
            "name": CharField,
            "approved": BooleanField,
        }
        for field in WishListItem._meta.fields:
            assert isinstance(
                field, types_map[field.name]
            ), f"Pole '{field.name}' nie jest typu {types_map[field.name]}"

    def test_wish_list_is_foreign_key_to_wishlist(self):
        assert (
            WishListItem._meta.get_field("wish_list").remote_field.model == WishList
        ), "Pole wish_list nie jest kluczem obcym do modelu WishList"
