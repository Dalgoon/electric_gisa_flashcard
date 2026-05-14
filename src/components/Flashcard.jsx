import React, { useState, useEffect } from 'react';
import classNames from 'classnames';
import { CheckCircle } from 'lucide-react';
import TextWithMath from './TextWithMath';
import './Flashcard.css';

const Flashcard = ({ card, isFlipped, setIsFlipped, isMemorized }) => {
  // Reset flip state when card changes
  useEffect(() => {
    setIsFlipped(false);
  }, [card, setIsFlipped]);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div 
      className={classNames('flashcard-container', { 'memorized': isMemorized })}
      onClick={handleFlip}
    >
      <div className={classNames('flashcard', { 'flipped': isFlipped })}>
        
        {/* Front Face */}
        <div className="flashcard-face flashcard-front">
          <div className="card-header">
            <span className="topic-badge">{card.topic}</span>
            {isMemorized && <CheckCircle size={24} color="#10b981" />}
          </div>
          <div className="card-content">
            <div>
              <TextWithMath text={card.question} />
            </div>
          </div>
          <div className="card-footer">
            Click to see the answer
          </div>
        </div>

        {/* Back Face */}
        <div className="flashcard-face flashcard-back">
          <div className="card-header">
            <span className="topic-badge">Answer</span>
            {isMemorized && <CheckCircle size={24} color="#10b981" />}
          </div>
          <div className="card-content">
            <div>
              <TextWithMath text={card.answer} />
            </div>
          </div>
          <div className="card-footer">
            Click to see the question
          </div>
        </div>

      </div>
    </div>
  );
};

export default Flashcard;
