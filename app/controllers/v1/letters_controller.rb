class V1::LettersController < ApplicationController
  def index
    @letters = Letter.all

    render json: @letters.to_json
  end

  def show
    @word_of_letter = Word.where(letter_id: params[:id])

    render json: @word_of_letter.to_json
  end

  def create
    @letter = Letter.create(character: params[:character])

    render json: @letter.to_json
  end
end
