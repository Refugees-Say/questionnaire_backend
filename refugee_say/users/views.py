from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User


from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        if not request.POST.get('password', None):
            request.POST['password'] = User.objects.make_random_password()
        return super(UserViewSet, self).create(request, *args, **kwargs)


# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
#
#
# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False
#
#     def get_redirect_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})
#
#
# class UserUpdateView(LoginRequiredMixin, UpdateView):
#
#     fields = ['name', ]
#
#     # we already imported User in the view code above, remember?
#     model = User
#
#     # send the user back to their own page after a successful update
#     def get_success_url(self):
#         return reverse('users:detail',
#                        kwargs={'username': self.request.user.username})
#
#     def get_object(self):
#         # Only get the User record for the user making the request
#         return User.objects.get(username=self.request.user.username)
#
#
# class UserListView(LoginRequiredMixin, ListView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
