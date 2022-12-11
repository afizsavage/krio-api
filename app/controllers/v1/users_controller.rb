class V1::UsersController < ApplicationController
  def index
    @users = User.all

    render json: @users.to_json
  end

  def create
    @user = User.create(first_name: params[:first_name], last_name: params[:last_name], role: params[:role])

    render json: @user.to_json
  end
end
