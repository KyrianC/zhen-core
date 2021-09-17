from dj_rest_auth.views import LoginView


class CustomLoginView(LoginView):
    """
    change inconsistent dictionary key in the response, for better handling in client
    Originaly refresh and token view's key of simple_jwt are "access" and "refresh"
    but dj_rest_auth login view give "access_token" and "refresh_token" instead
    make everything consistent to "access" and "refresh" only
    """

    def get_response(self):
        original_response = super().get_response()
        original_response.data["access"] = original_response.data.pop("access_token")
        original_response.data["refresh"] = original_response.data.pop("refresh_token")
        return original_response
