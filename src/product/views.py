from django.db.models import Prefetch, Subquery, OuterRef
from django.shortcuts import render
from .form import ProductForm, ProductImageFormSet
from .models import ProductImage, Product, Category


# Create your views here.

def product_create(request):
    form = ProductForm()
    if request.POST:
        form = ProductForm(request.POST or None)
        # formset = ProductImageFormSet()
        print(form, form.is_valid())
        if form.is_valid():
            product = form.save(commit=False)
            product.description = request.POST.get('description')
            product.save()
            files = request.POST.getlist('file')
            for f in files:
                ProductImage.objects.create(
                    product=product,
                    image=f
                )
    context = {
        "form": form,
        # "formset": formset
    }
    return render(request, 'create.html', context)


def product_details(request, product_id):
    product = Product.objects.filter(id=product_id).select_related('category', 'city', 'user').prefetch_related(
        Prefetch('productimage_set', queryset=ProductImage.objects.all())
    ).annotate(
        parent_category_name=Subquery(Category.objects.filter(id=OuterRef('category__parent_id')).values('name'))
    )

    format_product = []
    for p in product:
        images = [image.image for image in p.productimage_set.all()]
        format_product.append({
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": p.price,
            "user": p.user.username,
            "phone_number": p.user.phone_number,
            "user_image": p.user.photo,
            "city": p.city.name,
            "category": p.category.name,
            "parent_category": p.parent_category_name,
            "discaunt": p.discaunt,
            "condition": p.candition,
            "status": p.status,
            "created_date": p.created_date,
            "images": images
        })

    context = {
        "product": format_product
    }

    return render(request, 'productdetails.html', context)
