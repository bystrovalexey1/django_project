from .models import Product


class ProductServices:
    @staticmethod
    def all_product_in_category(category_id):
        return Product.objects.filter(category_id=category_id).select_related(
            "category",
        )
