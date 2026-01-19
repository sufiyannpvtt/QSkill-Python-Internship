# API Design – Sentiment Analysis Service

## Endpoint

`POST /api/analyze`

## Request Format

{
"text": "I love this product"
}

Response Format
{
"sentiment": "Positive",
"polarity": 0.82,
"confidence": 82,
"emoji": "😊"
}

Design Principles

RESTful API

JSON-based communication

Lightweight and fast

Frontend independent

Security

Rate limiting enabled (Flask-Limiter)

Input validation

Safe default responses

Usage

Web applications

Review analysis

Feedback systems

Customer sentiment monitoring
