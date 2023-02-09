class V1::LettersController < ApplicationController
  def index
    @letters = Letter.all

    render json: @letters.order(:character).to_json
  end

  def show
    @word_of_letter = Word.where(letter_id: params[:id])

    render json: @word_of_letter.to_json
  end

  def create
    @letter = Letter.create(letters_params)

    render json: @letter.to_json
  end

  private

  def letters_params
    params.require(:letter).permit(:character)
  end
end
