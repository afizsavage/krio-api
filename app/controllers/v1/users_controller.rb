class V1::UsersController < ApplicationController
  def index
    @users = User.all

    render json: @users.to_json
  end

  def create
    @user = User.create(users_params)

    if @user.save
      render json: @user.to_json, status: :created
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end

  private

  def users_params
    params.require(:user).permit(:first_name, :last_name, :role)
  end
end
