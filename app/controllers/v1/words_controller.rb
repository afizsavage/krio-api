class V1::WordsController < ApplicationController
  def index
    @words = Word.all

    render json: @words.to_json
  end

  def create
    @word = Word.create(word_params)

    if @word.save
      render json: @word.to_json, status: :created
    else
      render json: @word.errors, status: :unprocessable_entity
    end
  end

  private

  def word_params
    params.require(:word).permit(
      :title, :letter_id, :user_id,
      defination_attributes: %i[define example_statement approval_status user_id]
    )
  end
end
