class RoleMixin:
    """
    A mixin for ModelAdmin.
    """

    @property
    def roles(self):
        raise NotImplementedError

    def dispatch(self, attr, request, *args, **kw):
        user = request.user
        role = user.role_choices[user.role]
        role_cls = getattr(self.roles, role)
        if hasattr(role_cls, attr):
            func = getattr(role_cls, attr)
            return func(self, request, *args, **kw)
        return getattr(super(), attr)(request, *args, **kw)

    def get_model_perms(self, request):
        return self.dispatch('get_model_perms', request)
    
    def has_add_permission(self, request):
        return self.get_model_perms(request).get('add')

    def has_change_permission(self, request, obj=None):
        return self.get_model_perms(request).get('change')

    def has_delete_permission(self, request, obj=None):
        return self.get_model_perms(request).get('delete')

    def get_queryset(self, request):
        return self.dispatch('get_queryset', request)
    
    def get_exclude(self, request, obj=None):
        return self.dispatch('get_exclude', request, obj=obj)

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        exclude = self.get_exclude(request) or []
        return [f for f in list_display if f not in exclude]

    def super(self):
        return super()
