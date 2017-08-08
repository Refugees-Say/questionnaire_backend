from rest_framework import authentication, exceptions
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import User

from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrieves User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        random_pass = None
        if not request.data.get('password', None):
            random_pass = User.objects.make_random_password()
            request.data['password'] = random_pass
        response = super().create(request, *args, **kwargs)
        if random_pass:
            response.data['random_pass'] = random_pass
        return response


class UserAuthentication(authentication.SessionAuthentication):

    def authenticate_header(self, request):
        return super().authenticate_header(request)

    def authenticate(self, request):
        return super().authenticate(request)

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
