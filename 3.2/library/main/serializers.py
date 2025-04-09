from rest_framework import serializers
from .models import Book, Order



class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'year']

    #доп задание (пока не получилось :-( )
    #def to_representation(self, instance):
    #    data = super().to_representation(instance)
    #    data['orders_count'] = instance.author
    #    return data


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = ['id', 'user_name', 'days_count', 'date', 'books']

    #доп задание
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['books'] = [{'author': book.author, 'title': book.title, 'year': book.year} for book in instance.books.all()]
        return data