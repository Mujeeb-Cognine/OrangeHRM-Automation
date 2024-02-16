from _Wrapper.BaseClass import BaseClass


class BaseAPIUtils(BaseClass):

    def api_url(self, endpoint):
        try:
            orghrm_base_url = self.get_base_url()
            api_url = f'{orghrm_base_url}{endpoint}'
            self.logger.info(f"API URL generated successfully: {api_url}")
            return api_url
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            return None

    def bearer(self):
        try:
            bearer_token = self.get_bearer_token()
            self.logger.info("Bearer token retrieved successfully.")
            return bearer_token
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            return None
