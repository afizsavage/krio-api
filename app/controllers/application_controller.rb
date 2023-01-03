class ApplicationController < ActionController::API
  include ActionController::MimeResponds

  before_action :configure_permitted_parameters, if: :devise_controller?

  protected

  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up) do |u|
      u.permit(:first_name,
               :last_name, :email, :password)
    end
  end

  respond_to :json
end
