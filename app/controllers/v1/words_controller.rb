class V1::WordsController < ApplicationController
  def index
    @words = Word.all

    render json: @words.to_json
  end

  def create
    @word = Word.create(words_params)

    if @word.save
      render json: @word.to_json, status: :created
    else
      render json: @word.errors, status: :unprocessable_entity
    end
  end

  private

  def words_params
    params.require(:word).permit(:title, :letter, :user)
  end
end
