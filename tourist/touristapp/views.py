from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


from rest_framework import viewsets
from .models import User, Channel, Location, Category, Tag, Flag, Message
from .serializers import UserSerializer, ChannelSerializer, LocationSerializer, CategorySerializer, TagSerializer, FlagSerializer, MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Для остальных моделей повторите подобные классы, заменяя имена классов и ссылки на модели и сериализаторы

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class FlagViewSet(viewsets.ModelViewSet):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


from django.shortcuts import render, get_object_or_404


def message_list(request):
    messages = Message.objects.all()[:100]  # получите первые 100 сообщений
    return render(request, 'message_list.html', {'messages': messages})

def message_detail(request, message_id):
    message = get_object_or_404(Message, telegram_id=message_id)
    return render(request, 'message_detail.html', {'message': message})