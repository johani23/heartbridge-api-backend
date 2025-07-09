import React from 'react';
import { useNavigate } from 'react-router-dom';

function Landing() {
  const navigate = useNavigate();

  return (
    <div className="app-container">
      <h1>مرحبًا بك في Heartbridge</h1>
      <p>حلّل علاقتك بذكاء قبل ما تندم.</p>
      <button className="analyze-button" onClick={() => navigate('/quiz')}>
        ابدأ التحليل
      </button>
    </div>
  );
}

export default Landing;