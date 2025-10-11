import torch
import torch.nn as nn
import torch.nn.functional as F

# Simple dataset (text corpus)
text = "hello how are you hello how is your day hello how are we"
words = text.split()

# Build vocabulary
vocab = sorted(set(words))
word_to_ix = {word: i for i, word in enumerate(vocab)}
ix_to_word = {i: word for word, i in word_to_ix.items()}

# Prepare training data (predict next word)
data = []
for i in range(len(words) - 2):
    input_seq = torch.tensor([word_to_ix[words[i]], word_to_ix[words[i+1]]])
    target = torch.tensor(word_to_ix[words[i+2]])
    data.append((input_seq, target))

# Define a small model
class TinyLM(nn.Module):
    def __init__(self, vocab_size, embedding_dim=10, hidden_dim=20):
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(embedding_dim * 2, hidden_dim)
        self.linear2 = nn.Linear(hidden_dim, vocab_size)
    
    def forward(self, inputs):
        embeds = self.embeddings(inputs).view(1, -1)
        out = F.relu(self.linear1(embeds))
        out = self.linear2(out)
        return out

# Train it
model = TinyLM(len(vocab))
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(500):
    total_loss = 0
    for input_seq, target in data:
        model.zero_grad()
        logits = model(input_seq)
        loss = loss_fn(logits, target.unsqueeze(0))
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.3f}")

# Try predicting the next word
def predict_next(word1, word2):
    with torch.no_grad():
        inputs = torch.tensor([word_to_ix[word1], word_to_ix[word2]])
        logits = model(inputs)
        predicted_idx = torch.argmax(logits, dim=1).item()
        return ix_to_word[predicted_idx]

print("\nPrediction:")
print("hello how →", predict_next("hello", "how"))
print("how are →", predict_next("how", "are"))
print("your day →", predict_next("your", "day"))
