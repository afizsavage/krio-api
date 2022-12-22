class V1::DefinationsController < ApplicationController
  def index
    @definations = Defination.limit(5).order('RANDOM()')

    render json: @definations.to_json
  end

  def create
    @defination = Defination.create(defination_params)

    render json: @defination.to_json
  end

  private

  def defination_params
    params.require(:defination).permit(:define, :example_statement, :approval_status, :user_id, :word_id)
  end
end
